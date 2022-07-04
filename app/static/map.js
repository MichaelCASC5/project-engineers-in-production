/**
 * @param  {H.Map} map      A HERE Map instance within the application
 */

 function addMarkersToMap(map) {

  var romeMarker = new H.map.Marker({lat:41.9, lng: 12.5});
  map.addObject(romeMarker);

  var londonMarker = new H.map.Marker({lat:51.5008, lng:-0.1224});
  map.addObject(londonMarker);

  var colimaMarker = new H.map.Marker({lat:19.243919, lng:-103.728539});
  map.addObject(colimaMarker);

  var mexicoCityMarker = new H.map.Marker({lat:19.432608, lng:-99.133209});
  map.addObject(mexicoCityMarker);

  var nycMarker = new H.map.Marker({lat:40.712776, lng:-74.005974});
  map.addObject(nycMarker);

}

 function setInteractive(map){
    // get the vector provider from the base layer
    var provider = map.getBaseLayer().getProvider();
  
    // get the style object for the base layer
    var style = provider.getStyle();
  
    var changeListener = (evt) => {
      if (style.getState() === H.map.Style.State.READY) {
        style.removeEventListener('change', changeListener);
  
        // enable interactions for the desired map features
        style.setInteractive(['places', 'places.populated-places'], true);
  
        // add an event listener that is responsible for catching the
        // 'tap' event on the feature and showing the infobubble
        provider.addEventListener('tap', onTap);
      }
    };
    style.addEventListener('change', changeListener);
  }
  
  /**
   * Boilerplate map initialization code starts below:
   */
  
  //Step 1: initialize communication with the platform
  // In your own code, replace variable window.apikey with your own apikey
  var platform = new H.service.Platform({
    apikey: 'OGQ_34-JMA9MvSwhYbTPKIEE_pp3fIZatWN0cDIXF90'
  });
  var defaultLayers = platform.createDefaultLayers();
  
  //Step 2: initialize a map
  var map = new H.Map(document.getElementById('map'),
    defaultLayers.vector.normal.map, {
    center: {lat: 33.1036276975251, lng:  -39.85791020719383},
    zoom: 2,
    pixelRatio: window.devicePixelRatio || 1
  });
  // add a resize listener to make sure that the map occupies the whole container
  window.addEventListener('resize', () => map.getViewPort().resize());
  
  //Step 3: make the map interactive
  // MapEvents enables the event system
  // Behavior implements default interactions for pan/zoom (also on mobile touch environments)
  var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
  
  // Create the default UI components
  var ui = H.ui.UI.createDefault(map, defaultLayers);
  
  var bubble;
  /**
   * @param {H.mapevents.Event} e The event object
   */
  function onTap(evt) {
    // calculate infobubble position from the cursor screen coordinates
    let position = map.screenToGeo(
      evt.currentPointer.viewportX,
      evt.currentPointer.viewportY
    );
    // read the properties associated with the map feature that triggered the event
    let props = evt.target.getData().properties;
  
    // create a content for the infobubble
    let content = '<div style="width:250px">It is a ' + props.kind + ' ' + (props.kind_detail || '') +
      (props.population ? '<br /> population: ' + props.population : '') +
      '<br /> local name is ' + props['name'] +
      (props['name:ar'] ? '<br /> name in Arabic is '+ props['name:ar'] : '') + '</div>';
  
    // Create a bubble, if not created yet
    if (!bubble) {
      bubble = new H.ui.InfoBubble(position, {
        content: content
      });
      ui.addBubble(bubble);
    } else {
      // Reuse existing bubble object
      bubble.setPosition(position);
      bubble.setContent(content);
      bubble.open();
    }
  }
  
  // Now use the map as required...
  setInteractive(map);

  window.onload = function () {
    addMarkersToMap(map);
  }