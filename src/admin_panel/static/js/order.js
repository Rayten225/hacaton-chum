document.addEventListener('DOMContentLoaded', function() {
    const productsTextarea = document.getElementById('products');
    const totalPriceInput = document.getElementById('total-price');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Обновление отображения заказа
    function updateOrderSummary() {
        if (cart.length > 0) {
            productsTextarea.value = cart.map((item, index) => `${index + 1}. ${item.quantity} x ${item.product} - ${item.quantity * item.price}₽`).join('\n');
            const total = cart.reduce((sum, item) => sum + item.quantity * item.price, 0);
            totalPriceInput.value = `${total}₽`;
        } else {
            productsTextarea.value = "Корзина пуста.";
            totalPriceInput.value = "0₽";
        }
    }

    // Отображение товаров с кнопками удаления
    function renderCartWithRemoveButtons() {
        const productsContainer = document.getElementById('products-container') || document.createElement('div');
        productsContainer.id = 'products-container';
        productsContainer.innerHTML = '';
        productsContainer.style.marginTop = '20px';

        cart.forEach((item, index) => {
            const itemRow = document.createElement('div');
            itemRow.style.display = 'flex';
            itemRow.style.justifyContent = 'space-between';
            itemRow.style.marginBottom = '10px';

            const itemDescription = document.createElement('span');
            itemDescription.textContent = `${item.quantity} x ${item.product} - ${item.quantity * item.price}₽`;

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Удалить';
            removeButton.style.marginLeft = '10px';
            removeButton.addEventListener('click', () => {
                removeItem(index);
            });

            itemRow.appendChild(itemDescription);
            itemRow.appendChild(removeButton);
            productsContainer.appendChild(itemRow);
        });

        const parent = totalPriceInput.parentElement;
        if (!document.getElementById('products-container')) {
            parent.insertBefore(productsContainer, totalPriceInput);
        }
    }

    // Удаление товара из корзины
    function removeItem(index) {
        if (index >= 0 && index < cart.length) {
            cart.splice(index, 1);
            localStorage.setItem('cart', JSON.stringify(cart));
            updateOrderSummary();
            renderCartWithRemoveButtons();
        }
    }

    // Инициализация корзины
    updateOrderSummary();
    renderCartWithRemoveButtons();

    // Обработка отправки заказа
    const orderForm = document.querySelector('.order-form');
    orderForm.addEventListener('submit', function(event) {
        event.preventDefault();

        if (cart.length === 0) {
            alert('Корзина пуста. Невозможно оформить заказ.');
            return;
        }

        const orderDetails = {
            order: JSON.stringify(cart),
            price: totalPriceInput.value,
            deadline: document.getElementById('deadline').value,
            organization: document.getElementById('organization').value,
            FIO: document.getElementById('contact-name').value,
            number: document.getElementById('phone').value,
            address: document.getElementById('address').value,
            email: document.getElementById('email').value,
        };

        // Сохраняем заказ в историю
        // const orderHistory = JSON.parse(localStorage.getItem('orderHistory')) || [];
        // orderHistory.push({
        //     products: cart,
        //     totalPrice: totalPriceInput.value,
        //     date: new Date().toLocaleString(),
        // });
        // localStorage.setItem('orderHistory', JSON.stringify(orderHistory));

                // $.ajax({
                //     url: '/api/orders',
                //     type: 'POST',
                //     contentType: 'application/json',
                //     data: JSON.stringify({order: order, price: price, deadline: deadline, organization: organization, FIO: FIO, number: number, address: address, email: email}), 
                //     success: function (response) {
                //         $('#order').text(response.message);
                //     },
                //     error: function (xhr) {
                //         const response = JSON.parse(xhr.responseText);
                //         $('#order').text(response.message);
                //     }
                // });

        // Очищаем корзину
        alert('Ваш заказ успешно оформлен!');
        localStorage.removeItem('cart');
        cart = [];
        orderForm.reset();
        updateOrderSummary();
        renderCartWithRemoveButtons();
    });
});
