import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import GoogleMapKey from './key.json';
import Polyline from "./Polyline";
import Marker from "./Marker";

class SimpleMap extends Component {

  constructor(){
    super();
    this.state = {
      start: {lat: 0, lng: 0, title: "start"},
      destination: {lat: 0, lng: 0, title: "destination"},
      mapLoaded: false
    };
    this.isStart = true;
  }

  static defaultProps = {
    center: {
      lat: 48.1496636,
      lng: 11.5656715
    },
    zoom: 12,
    greenMarker: "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
    redMarker: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
  };

  onClick = ({x, y, lat, lng, event}) => {
    if(this.isStart === true){
      this.setState({start:{lat: lat, lng: lng, title: "start", icon: this.props.redMarker}});
      this.isStart = false;
    }
    else if(this.isStart === false) {
      this.setState({destination:{lat: lat, lng: lng, title: "destination", icon: this.props.greenMarker}});
      this.isStart = true;
    }
  }

  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '60vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: GoogleMapKey.key }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          onClick={this.onClick}
          onGoogleApiLoaded ={({ map, maps }) => { this.setState({ map: map, maps:maps, mapLoaded: true }) }}
          yesIWantToUseGoogleMapApiInternals
        >

        { this.state.mapLoaded && <Polyline map={this.state.map} maps={this.state.maps} /> }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.start} /> }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.destination} /> }

        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;