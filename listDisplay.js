//     Tech case for Cybel Angel
//
//     Re write JS code as if it is served via distant API server
//
//     Author: Mariya Rychkova


function display() {

    // Create ordered list HTML element inside the body tag
    document.getElementsByTagName('body')[0].innerHTML += '<ol id="categories"></ol>';

    const ul = document.getElementById('categories');
    const url = 'GET /categories';

    // Fetch the data on the distant server url
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            let categories = data.results;

                // Iterate through all the categories fetched and
                return categories.map(function(category) {
                    let li = document.createElement('li');
                    li.innerHTML = category.name;
                    ul.appendChild(li);
      })
    })
    // En cas d'erreur
    .catch(function(error) {
      console.log(error);
    });

display();
}
