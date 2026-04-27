// Snippet de Verificación de Selectores
function verificarSelectores() {
    const lista = ['#user-name', '#password', '#login-button'];
    
    lista.forEach(sel => {
        const el = document.querySelector(sel);
        if (el) {
            el.style.backgroundColor = 'khaki';
            el.style.border = '2px solid orange';
            console.log(`✅ OK: ${sel}`);
        } else {
            console.warn(`⚠️ NO ENCONTRADO: ${sel}`);
        }
    });
}

verificarSelectores();