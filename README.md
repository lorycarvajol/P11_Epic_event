
## Description du Projet

Epic Events CRM est une application de gestion de la relation client (CRM) développée pour la société Epic Events, qui organise des événements pour ses clients. Cette application permet de collecter et de traiter les données des clients, contrats, et événements, tout en facilitant la communication entre les différents départements de l'entreprise (Commercial, Support, Gestion).

## Fonctionnalités Principales

- **Gestion des Clients :** Créer, mettre à jour et supprimer les informations des clients.
- **Gestion des Contrats :** Gérer les contrats signés avec les clients, y compris le suivi des paiements.
- **Gestion des Événements :** Organiser et suivre les événements associés aux contrats des clients.
- **Journalisation des Erreurs :** Intégration de Sentry pour capturer les erreurs et exceptions en temps réel.
- **Sécurité :** Mise en œuvre des pratiques de sécurité avancées, y compris la prévention des injections SQL et l'application du principe du moindre privilège.

## Diagramme UML

Le diagramme UML ci-dessous illustre les principales classes du système et leurs relations :

![Diagramme UML](diagramme_uml.png)

## Modèle de Données

### Client

- **id:** Identifiant unique (auto-incrémenté)
- **nom_complet:** Nom complet du client
- **email:** Adresse email unique
- **telephone:** Numéro de téléphone
- **entreprise:** Nom de l'entreprise du client
- **date_creation:** Date de création du profil client
- **dernier_contact:** Date du dernier contact avec le client

### Contrat

- **id:** Identifiant unique (auto-incrémenté)
- **client:** Référence au client associé
- **contact_commercial:** Référence au collaborateur commercial responsable du contrat
- **montant_total:** Montant total du contrat
- **montant_restant:** Montant restant à payer
- **date_creation:** Date de création du contrat
- **statut:** Statut du contrat (signé ou non signé)

### Événement

- **id:** Identifiant unique (auto-incrémenté)
- **contrat:** Référence au contrat associé
- **responsable_support:** Référence au collaborateur support responsable de l'événement
- **date_debut:** Date de début de l'événement
- **date_fin:** Date de fin de l'événement
- **lieu:** Lieu de l'événement

### Collaborateur

- **id:** Identifiant unique (auto-incrémenté)
- **nom:** Nom du collaborateur
- **email:** Adresse email unique
- **role:** Rôle du collaborateur (Commercial, Support, Gestion)
- **date_embauche:** Date d'embauche du collaborateur

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votrecompte/epic_events_crm.git
   cd epic_events_crm
   ```

`</code></div>``</div></pre>`

2. **Créer un environnement virtuel :**
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copier le code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python3 -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   </code></div></div></pre>
3. **Installer les dépendances :**
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copier le code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
   </code></div></div></pre>
4. **Appliquer les migrations :**
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copier le code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python manage.py migrate
   </code></div></div></pre>
5. **Lancer l'application :**
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copier le code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python manage.py runserver
   </code></div></div></pre>

## Contributions

Les contributions sont les bienvenues. Merci de soumettre une demande de fusion (Pull Request) via GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE]() pour plus de détails.
