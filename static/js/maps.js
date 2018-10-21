var map;
var service;
var infoWindow;

function initMap() {
    var mapCenter = new google.maps.LatLng(-23.5489, -46.6388);

    map = new google.maps.Map(document.getElementById('map'), {
        center: mapCenter,
        zoom: 11
    });

    infoWindow = new google.maps.InfoWindow();
    service = new google.maps.places.PlacesService(map);

    // locatePlaceInMap('Alto da Boa Vista, São Paulo - SP');
    // locatePlaceInMap('Barra Funda, São Paulo - SP');
    // locatePlaceInMap('Cidade Tiradentes, São Paulo - SP');
}

function locatePlaceInMap(query) {
    var request = {
        query: query,
        fields: ['name', 'geometry']
    };

    service.findPlaceFromQuery(request, queryCallback);
}

function queryCallback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            var place = results[i];
            createMarker(results[i]);
        }
    }
}

function createMarker(place) {
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
    });

    google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(place.name);
        infoWindow.open(map, this);
    });
}
