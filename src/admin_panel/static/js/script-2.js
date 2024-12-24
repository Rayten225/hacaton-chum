document.addEventListener('DOMContentLoaded', function () {
    // Переменные для конструктора пряников
    const sizeSelect = document.getElementById('size');
    const flavorGroup = document.getElementById('flavor-group');
    const packagingGroup = document.getElementById('packaging-group');
    const imprintGroup = document.getElementById('imprint-group');
    const packagingSelect = document.getElementById('packaging');
    const imprintSelect = document.getElementById('imprint');
    const typeGroup = document.getElementById('type-group');

    // Изначально скрываем группы выбора
    if (flavorGroup) flavorGroup.style.display = 'none';
    if (packagingGroup) packagingGroup.style.display = 'none';
    if (imprintGroup) imprintGroup.style.display = 'none';
    if (typeGroup) typeGroup.style.display = 'none';

    // Проверяем наличие элементов перед настройкой событий
    if (sizeSelect) {
        sizeSelect.addEventListener('change', function () {
            const size = sizeSelect.value;

            // Отображение группы "Вкус"
            if (flavorGroup) {
                flavorGroup.style.display = (size === '350g' || size === '700g' || size === '1000g') ? 'block' : 'none';
            }

            // Отображение и заполнение группы "Упаковка"
            if (packagingGroup) {
                packagingGroup.style.display = (size === '1000g') ? 'block' : 'none';
                if (packagingSelect) {
                    packagingSelect.innerHTML = (size === '1000g') ? `
                        <option value="Обычная упаковка">Обычная упаковка</option>
                        <option value="Сувенирная коробка">Сувенирная коробка</option>
                    ` : `
                        <option value="Обычная упаковка">Обычная упаковка</option>
                    `;
                }
            }

            // Отображение группы "Тип пряника"
            if (typeGroup) {
                typeGroup.style.display = (size === '350g' || size === '700g' || size === '1000g') ? 'block' : 'none';
            }

            // Отображение группы "Оттиск"
            if (imprintGroup) {
                imprintGroup.style.display = (size === '700g' || size === '1000g') ? 'block' : 'none';
            }
        });
    }

    if (imprintSelect) {
        imprintSelect.addEventListener('change', function () {
            const imageUploadGroup = document.getElementById('image-upload-group');
            if (imageUploadGroup) {
                imageUploadGroup.style.display = (imprintSelect.value === 'custom') ? 'block' : 'none';
            }
        });
    }

    // Функция для добавления товара в корзину с учетом одинаковых позиций
function addToCart(product, quantity, price, additionalDetails = {}) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Проверяем, есть ли товар с таким же названием в корзине
    const existingItemIndex = cart.findIndex(item => item.product === product);

    if (existingItemIndex > -1) {
        // Если товар уже есть, обновляем количество
        cart[existingItemIndex].quantity += quantity;
    } else {
        // Если товара нет, добавляем его как новый
        cart.push({ product, quantity, price, ...additionalDetails });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
}

    // Функция для обновления сообщения о количестве товаров в корзине
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.product').forEach(product => {
            product.style.height = `${product.scrollHeight}px`;
        });
    });
    function updateCartMessage(productContainer, productName, quantity) {
        let messageElement = productContainer.querySelector('.add-to-cart-message');
        if (!messageElement) {
            messageElement = document.createElement('p');
            messageElement.classList.add('add-to-cart-message');
            messageElement.style.color = '#c36e32';
            productContainer.appendChild(messageElement);
            messageElement.dataset.totalQuantity = 0; // Инициализация общего количества
        }
    
        const currentQuantity = parseInt(messageElement.dataset.totalQuantity) || 0;
        const newQuantity = currentQuantity + quantity;
        messageElement.dataset.totalQuantity = newQuantity;
    
        messageElement.textContent = `${productName} (${newQuantity} шт.) добавлен(ы) в корзину.`;
    
        // Плавно показываем сообщение
        messageElement.classList.add('show');
    
        // Увеличиваем высоту родительского контейнера
        productContainer.style.height = `${productContainer.scrollHeight}px`;
    }

    // Обработка кнопок добавления в корзину
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Предотвращаем стандартное поведение

            const productContainer = button.parentElement;
            const productName = button.getAttribute('data-product');

            if (productName === 'Конструктор пряников') {
                // Логика для конструктора пряников
                const size = sizeSelect?.value || '';
                const flavor = document.getElementById('flavor')?.value || '';
                const packaging = packagingSelect?.value || '';
                const type = document.getElementById('type')?.value || '';
                const imprint = imprintSelect?.value || '';

                let price = 0;
                switch (size) {
                    case '100g':
                        price = 100;
                        break;
                    case '150g':
                        price = 150;
                        break;
                    case '350g':
                        price = 350;
                        break;
                    case '700g':
                        price = 700;
                        break;
                    case '1000g':
                        price = 1000;
                        break;
                }

                if (!size || (size === '350g' || size === '700g' || size === '1000g') && (!flavor || !type || (size === '1000g' && !packaging))) {
                    alert('Пожалуйста, заполните все поля конструктора.');
                    return;
                }

                const productNameDetails = `Пряник (${size}, ${flavor}, ${packaging}, ${type}, ${imprint})`;
                addToCart(productNameDetails, 1, price, { size, flavor, packaging, type, imprint });
                updateCartMessage(productContainer, productNameDetails, 1);
            } else {
                // Логика для каталога
                const quantityInput = productContainer.querySelector('.product-quantity');
                const quantity = parseInt(quantityInput?.value) || 1;

                if (quantity < 1) {
                    alert('Укажите корректное количество!');
                    return;
                }

                const price = parseFloat(productContainer.querySelector('.product-price')?.getAttribute('data-price')) || 0;

                updateCartMessage(productContainer, productName, quantity);

                addToCart(productName, quantity, price);
            }
        });
    });
});