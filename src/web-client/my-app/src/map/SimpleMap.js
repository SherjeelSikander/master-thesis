import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import GoogleMapKey from './key.json';
import Polyline from "./Polyline";
import Marker from "./Marker";
import MapOperations from "./MapOperations"

class SimpleMap extends Component {

  constructor(){
    super();
    this.state = {
      start: {lat: 0, lng: 0, title: "start"},
      destination: {lat: 0, lng: 0, title: "destination"},
      mapLoaded: false
    };
    this.selectStart = false;
    this.selectDestination = false;
  }

  componentWillReceiveProps(nextProps){
    if(nextProps.operation === MapOperations.operations.selectStart) {
      this.selectStart = true;
      this.selectDestination = false;
    }
    if(nextProps.operation === MapOperations.operations.selectDestination) {
      this.selectDestination = true;
      this.selectStart = false;
    }
    if(nextProps.path && nextProps.path.length > 2){
      this.setState({path:nextProps.path})
    }
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
    if(this.selectStart === true){
      this.setState({start:{lat: lat, lng: lng, title: "start", icon: this.props.redMarker}});
      this.selectStart = false;
      this.props.sendResult({start:{lat: lat, lng: lng, title: "start", icon: this.props.redMarker}});
    }
    else if(this.selectDestination === true) {
      this.setState({destination:{lat: lat, lng: lng, title: "destination", icon: this.props.greenMarker}});
      this.selectDestination = false;
      this.props.sendResult({destination:{lat: lat, lng: lng, title: "destination", icon: this.props.greenMarker}});
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

        { this.state.mapLoaded && <Polyline map={this.state.map} maps={this.state.maps} path={this.state.path}/> }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.start} /> }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.destination} /> }

        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;