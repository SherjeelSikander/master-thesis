import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import GoogleMapKey from './key.json';

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class SimpleMap extends Component {
  static defaultProps = {
    center: {
      lat: 48.1496636,
      lng: 11.5656715
    },
    zoom: 12
  };

  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '85vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: GoogleMapKey.key }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
        >
          <AnyReactComponent
            lat={48.1496636}
            lng={11.5656715}
            text={'Sherjeel Sikander'}
          />
        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;