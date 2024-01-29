var btnNewItem = document.querySelector('#new-item')
var productSection = document.querySelector('.new-product')

function addProduct() {
    const form = document.createElement('section')
    form.classList.add('.new-product')
}

btnNewItem.addEventListener('click', () => {
    productSection.classList.add('.new-product')
})


/* function addProduct() {
    // Clone do modelo da seção de produto
    var productSection = document.querySelector('.new-product').cloneNode(true);

    // Remover a classe para evitar a clonagem recursiva
    productSection.classList.remove('.new-product');

    // Limpar os valores dos campos clonados
    var inputs = productSection.querySelectorAll('input');
    inputs.forEach(input => (input.value = ''));

    // Adicionar a seção de produto clonada ao container
    document.getElementById('product-container').appendChild(productSection);
}
*/