// Obtenez les références des éléments DOM nécessaires
const addContactButton = document.querySelector('.add-contact-button');
const addContactModal = document.getElementById('add-contact-modal');
const closeModalButton = addContactModal.querySelector('.close');

// Gestionnaire d'événement pour ouvrir le modal
addContactButton.addEventListener('click', function() {
  addContactModal.style.display = 'block';
});

// Gestionnaire d'événement pour fermer le modal en cliquant sur le bouton de fermeture
closeModalButton.addEventListener('click', function() {
  addContactModal.style.display = 'none';
});

// Gestionnaire d'événement pour fermer le modal en cliquant en dehors de celui-ci
window.addEventListener('click', function(event) {
  if (event.target === addContactModal) {
    addContactModal.style.display = 'none';
  }
});
