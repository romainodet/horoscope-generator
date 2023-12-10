document.addEventListener("DOMContentLoaded", function () {
    const horoscopesContainer = document.getElementById("horoscopes");
    const toggleThemeButton = document.getElementById("toggle-theme");
    const body = document.body;

    // Fonction pour récupérer les horoscopes depuis l'API Flask
    function getHoroscope(signe) {
        fetch(`/horoscope/${signe}`)
            .then(response => response.json())
            .then(data => {
                const horoscopeDiv = document.createElement("div");
                horoscopeDiv.classList.add("horoscope-item");

                const signeTitre = document.createElement("h2");
                signeTitre.textContent = data.signe;
                horoscopeDiv.appendChild(signeTitre);

                const signeHoroscope = document.createElement("p");
                signeHoroscope.textContent = data.horoscope;
                horoscopeDiv.appendChild(signeHoroscope);

                horoscopesContainer.appendChild(horoscopeDiv);
            })
            .catch(error => {
                console.error(`Erreur lors de la récupération de l'horoscope pour ${signe} :`, error);
            });
    }

    // Liste des signes du zodiaque à afficher
    const signesDuZodiaque = ['bélier', 'taureau', 'gemeaux', 'cancer', 'lion', 'vierge', 'balance', 'scorpion', 'sagittaire', 'capricorne', 'verseau', 'poissons'];

    // Récupérer les horoscopes pour chaque signe et les afficher
    signesDuZodiaque.forEach(signe => {
        getHoroscope(signe);
    });
// Fonction pour activer le thème sombre
function activateDarkMode() {
    document.body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark'); // Enregistrez le choix de l'utilisateur dans le stockage local
 // Changez la couleur de remplissage de l'icône en mode sombre
    const themeIcon = document.getElementById('theme-icon');
    themeIcon.style.fill = '#333'; // Couleur sombre
}

// Fonction pour désactiver le thème sombre
function deactivateDarkMode() {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light'); // Enregistrez le choix de l'utilisateur dans le stockage local
        // Changez la couleur de remplissage de l'icône en mode clair
    const themeIcon = document.getElementById('theme-icon');
    themeIcon.style.fill = '#fff'; // Couleur claire
}

// Détecter les préférences de thème du système
const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)');

// Vérifiez si l'utilisateur a déjà fait un choix de thème
const userTheme = localStorage.getItem('theme');

if (userTheme === 'dark') {
    activateDarkMode();
} else if (userTheme === 'light') {
    deactivateDarkMode();
} else if (prefersDarkMode.matches) {
    activateDarkMode(); // Activer le thème sombre si le système préfère le mode sombre
}

// Écouter les changements de préférences de thème du système
prefersDarkMode.addEventListener('change', (event) => {
    if (event.matches) {
        activateDarkMode(); // Activer le thème sombre lorsque les préférences du système passent en mode sombre
    } else {
        deactivateDarkMode(); // Désactiver le thème sombre lorsque les préférences du système passent en mode clair
    }
});

// Gestion du bouton de basculement
const toggleButton = document.getElementById('toggle-theme');

toggleButton.addEventListener('click', () => {
    if (document.body.classList.contains('dark-mode')) {
        deactivateDarkMode(); // Si le mode sombre est actif, désactivez-le
    } else {
        activateDarkMode(); // Sinon, activez le mode sombre
    }
});
});