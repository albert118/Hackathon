let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8150, lng:  151.0011},
    zoom: 14
  });
}

function toggleSidebar() {
  if ($("#sidebar").css("left") === "0px") {
    $("#sidebar").css({left: -260});
    $("#toggle-icon").removeClass("fa-chevron-left");
    $("#toggle-icon").addClass("fa-chevron-right");
    $("#sidebar-hr").hide();
  } else {
    $("#sidebar").css({left: 0});
    $("#toggle-icon").removeClass("fa-chevron-right");
    $("#toggle-icon").addClass("fa-chevron-left");
    $("#sidebar-hr").show();
  }
}


      var sw = new mapboxgl.LngLat(150.69333046936686, -34.024318808594415);
      var ne = new mapboxgl.LngLat(151.35188893349857, -33.6825009519346);

      var llb = new mapboxgl.LngLatBounds(ne, sw);


      mapboxgl.accessToken = 'pk.eyJ1IjoidmlzdWFsaXNlZGF0YSIsImEiOiJjanV6Nnd6YTExNWo2M3lsNmp5eWhoZGhwIn0.6irQa7Mq9wSLfnnOMGNMPQ';

      var map = new mapboxgl.Map({
        container: 'map', // container id
        style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
        bounds: llb,
        center: [151.02260970148222,  -33.88217418212192],// starting position [lng, lat]
        zoom: 9, // starting zoom
        pitchWithRotate: false,
        dragRotate: false,
        touchZoomRotate: false,
        maxZoom: 20
      });


      //central
      var marker = new mapboxgl.Marker()
          .setOffset({x:0,y: 0})
          .setLngLat([151.206670, -33.882749])
          .addTo(map);
      //redfern
      var marker = new mapboxgl.Marker()
          .setOffset({x:0,y: 0})
          .setLngLat([151.19844, -33.892112])
          .addTo(map);

      //strathfield
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.094233,-33.8717015])
      .addTo(map);

      //lidcombe
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.0452425, -33.863813])
      .addTo(map);

      //auburn
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.0328107, -33.8493005])
      .addTo(map);


      //clyde
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.0170659, -33.835973])
      .addTo(map);

      //granville
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.0121496,-33.832905])
      .addTo(map);

      //harris park
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.0076473, -33.8233005])
      .addTo(map);

      //Parramatta
      var marker = new mapboxgl.Marker()
      .setOffset({x:0,y: 0})
      .setLngLat([151.0054012, -33.8175104])
      .addTo(map);

      map.on('load', function() {
  map.addLayer({
  'id': 'lines',
  'type': 'line',
  'source': {
  'type': 'geojson',
  'data': {
  'type': 'FeatureCollection',
  'features': [{
  'type': 'Feature',
  'properties': {
  'color': 'dodgerblue' // red
  },
  'geometry': {
  'type': 'LineString',
  'coordinates': [
    [151.206670, -33.882749],
    [151.19844, -33.892112],
    [151.094233,-33.8717015],
    [151.0452425, -33.863813],
    [151.0328107, -33.8493005],
    [151.0170659, -33.835973],
    [151.0121496,-33.832905],
    [151.0076473, -33.8233005],
    [151.0054012, -33.8175104]
  ]
  }
  }]
  }
  },
  'paint': {
  'line-width': 2,
  // Use a get expression (https://docs.mapbox.com/mapbox-gl-js/style-spec/#expressions-get)
  // to set the line-color to a feature property value.
  'line-color': ['get', 'color']
  }
  });
  });
