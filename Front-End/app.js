let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8150, lng:  151.0011},
    zoom: 14
  });
}

function toggleSidebar() {
  if ($("#sidebar").css("left") === "0px") {
    $("#sidebar").css({left: -230});
    $("#toggle-icon").removeClass("fa-chevron-left");
    $("#toggle-icon").addClass("fa-chevron-right");
  } else {
    $("#sidebar").css({left: 0});
    $("#toggle-icon").removeClass("fa-chevron-right");
    $("#toggle-icon").addClass("fa-chevron-left");
  }
}