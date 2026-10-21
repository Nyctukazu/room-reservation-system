import "./components/sidebar.js"
import "./components/navbar.js"

document.addEventListener('DOMContentLoaded', () => {
  // 1. Project Form Submission Handler
  const projectForm = document.getElementById('project-form');
  const alertBox = document.getElementById('form-alert');

  if (projectForm) {
    projectForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const title = document.getElementById('project-title').value.trim();
      const author = document.getElementById('project-author').value.trim();
      const description = document.getElementById('project-desc').value.trim();

      try {
        const response = await fetch('/api/projects', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ title, author, description })
        });

        const data = await response.json();

        if (response.ok) {
          showAlert(`Success! Project "${data.project.title}" created.`, 'success');
          projectForm.reset();
        } else {
          showAlert(`Error: ${data.error || 'Failed to create project.'}`, 'danger');
        }
      } catch (err) {
        console.error('Request failed:', err);
        showAlert('Network error while reaching /api/projects', 'danger');
      }
    });
  }

  function showAlert(message, type) {
    if (!alertBox) return;
    alertBox.className = `alert alert-${type} mt-3`;
    alertBox.textContent = message;
    alertBox.classList.remove('d-none');
    setTimeout(() => {
      alertBox.classList.add('d-none');
    }, 4000);
  }

  // 2. AI Generation Live Tester
  const aiBtn = document.getElementById('ai-test-btn');
  const aiPromptInput = document.getElementById('ai-prompt');
  const aiResponseBox = document.getElementById('ai-response-box');

  if (aiBtn && aiPromptInput && aiResponseBox) {
    aiBtn.addEventListener('click', async () => {
      const prompt = aiPromptInput.value.trim();
      if (!prompt) return;

      aiBtn.disabled = true;
      aiResponseBox.textContent = 'Generating response...';

      try {
        const res = await fetch('/api/ai/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt })
        });

        const data = await res.json();
        if (res.ok) {
          aiResponseBox.textContent = data.result;
        } else {
          aiResponseBox.textContent = `Error: ${data.error}`;
        }
      } catch (error) {
        aiResponseBox.textContent = 'Network error connecting to /api/ai/generate';
      } finally {
        aiBtn.disabled = false;
      }
    });
  }
});
