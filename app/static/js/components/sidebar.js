class AppSidebar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <aside class="main-sidebar">
                <h1>Hello There</h1>
            </aside>
        `;
    }
}

customElements.define('app-sidebar', AppSidebar);