// Initialize or update the cart from localStorage
let cart = JSON.parse(localStorage.getItem('cart')) || {};
updateCart();

// Event delegation to handle cart item additions dynamically
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.divpr').addEventListener('click', function(event) {
        if (event.target.classList.contains('cart')) {
            const idstr = event.target.id.toString();
            let qty, name;
            if (cart[idstr]) {
                cart[idstr][0] += 1;
            } else {
                qty = 1;
                name = document.getElementById('name' + idstr).innerText;
                cart[idstr] = [qty, name];
            }
            updateCart();
        } else if (event.target.classList.contains('minus') || event.target.classList.contains('plus')) {
            adjustItemQuantity(event.target);
        }
    });

    // Initialize popover for the cart
    $('#popcart').popover({
        html: true,
        trigger: 'focus'
    });
    updatePopover();
});

function updateCart() {
    let sum = 0;
    for (let item in cart) {
        sum += cart[item][0];
        let itemDisplay = document.getElementById('div' + item);
        if (itemDisplay) {
            itemDisplay.innerHTML = `<button id='minus${item}' class='btn btn-primary minus'>-</button>
                                     <span id='val${item}'>${cart[item][0]}</span>
                                     <button id='plus${item}' class='btn btn-primary plus'>+</button>`;
        }
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').textContent = sum;
    updatePopover();
}

function updatePopover() {
    let popStr = "<h5>Cart for your items in my shopping cart</h5><div class='mx-2 my-2'>";
    let i = 1;
    for (let item in cart) {
        popStr += `<b>${i}</b>. ${cart[item][1].slice(0, 19)}... Qty: ${cart[item][0]}<br>`;
        i++;
    }
    popStr += "</div><a href='/shop/checkout'><button class='btn btn-primary' id='checkout'>Checkout</button></a> "
            + "<button class='btn btn-primary' onclick='clearCart()' id='clearCart'>Clear Cart</button>";
    
    document.getElementById('popcart').setAttribute('data-content', popStr);
}

function clearCart() {
    localStorage.clear();
    cart = {};
    updateCart();
}

function adjustItemQuantity(button) {
    const id = button.id.slice(5);
    const action = button.classList.contains('minus') ? -1 : 1;
    if (cart['pr' + id]) {
        cart['pr' + id][0] = Math.max(0, cart['pr' + id][0] + action);
        document.getElementById('valpr' + id).textContent = cart['pr' + id][0];
        updateCart();
    }
}
