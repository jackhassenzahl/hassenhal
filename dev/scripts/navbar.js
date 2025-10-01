fetch('/templates/navbar.html')
  .then(response => response.text())
  .then(data => {
    document.getElementById('navigation').innerHTML = data;
  })
  .catch(error => console.error('Error loading navbar:', error));
