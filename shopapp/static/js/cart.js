let updateBtns = document.getElementsByClassName('update-cart')


for (let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        if (user === 'AnonymousUser'){
            console.log('Is not logged in')
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}


function updateUserOrder(productId, action) {
    url = 'http://127.0.0.1:8000/catalog/update_item/'

    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            location.reload()
        })
}