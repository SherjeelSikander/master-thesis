import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import GoogleMapKey from './key.json';
import Polyline from "./Polyline";

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class SimpleMap extends Component {

  constructor(){
    super();
    this.state = {
      start: {lat: 0, lng: 0},
      end: {lat: 0, lng: 0},
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
    this.setState({start:{lat: lat, lng: lng}});
  }

  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '85vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: GoogleMapKey.key }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          onClick={this.onClick}
          onGoogleApiLoaded ={({ map, maps }) => { this.setState({ map: map, maps:maps, mapLoaded: true }) }}
          yesIWantToUseGoogleMapApiInternals
        >

        { this.state.mapLoaded && <Polyline map={this.state.map} maps={this.state.maps} /> }
          
          <AnyReactComponent
            lat={this.state.start.lat}
            lng={this.state.start.lng}
            text={'Sherjeel Sikander'}
          />

        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;