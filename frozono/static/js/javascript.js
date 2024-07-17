
// Función para mostrar el mapa en la página de contacto
function iniciarMap(){
    var coord = {lat:-33.0092618 ,lng: -71.5425126};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}
