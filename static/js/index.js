function toggleContent(elementId) {
    var element = document.querySelector('.' + elementId);
    element.style.display = (element.style.display === 'none' || element.style.display === '') ? 'block' : 'none';
}