import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import GoogleMapKey from './key.json';
import Polyline from "./Polyline";
import Marker from "./Marker";

class SimpleMap extends Component {

  constructor(){
    super();
    this.state = {
      start: {lat: 0, lng: 0},
      end: {lat: 0, lng: 0},
      marker: {lat: 0, lng: 0},
      mapLoaded: false
    };
  }

  static defaultProps = {
    center: {
      lat: 48.1496636,
      lng: 11.5656715
    },
    zoom: 12
  };

  onClick = ({x, y, lat, lng, event}) => {
    this.setState({marker:{lat: lat, lng: lng}});
  }

  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '88vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: GoogleMapKey.key }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          onClick={this.onClick}
          onGoogleApiLoaded ={({ map, maps }) => { this.setState({ map: map, maps:maps, mapLoaded: true }) }}
          yesIWantToUseGoogleMapApiInternals
        >

        { this.state.mapLoaded && <Polyline map={this.state.map} maps={this.state.maps} /> }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.marker} /> }

        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;