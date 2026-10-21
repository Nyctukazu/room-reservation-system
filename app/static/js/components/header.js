class AppHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML =  `
            <header class="main-header">
                <h1>My App</h1>
            </header>
        `;
    }
}

customElements.define('app-header', AppHeader);