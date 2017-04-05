
// genre form answers to array and send to Django view
function genre_form() {
    var elements = document.getElementById("my-form").elements;
    var genres = [];
    for (var i = 0, element; element = elements[i++];) {
        if (element.checked) {
		          genres.push(Number(element.value))
        }
    }
    console.log(genres);

}
