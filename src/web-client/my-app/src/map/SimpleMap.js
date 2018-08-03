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
    if(nextProps.paths && nextProps.paths.length > 0){
      this.setState({paths:nextProps.paths})
    }
    if(nextProps.trees && nextProps.trees.length > 0){
      this.setState({trees:nextProps.trees})
    }
  }

  static defaultProps = {
    center: {
      lat: 48.1496636,
      lng: 11.5656715
    },
    zoom: 12,
    greenMarker: "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
    redMarker: "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
    tree: "https://maps.google.com/mapfiles/ms/micons/tree.png"
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
    if (this.state.mapLoaded && this.state.paths) {
      var that = this;
      var pathList = this.state.paths.map(function (path, index) {
        return <Polyline key={index} map={that.state.map} maps={that.state.maps} path={path} />;
      })
      console.log("Done")
    }
    if (this.state.mapLoaded && this.state.paths && this.state.paths.length > 1) {
      var that = this;
      var intermediateMarkerList = this.state.paths.map(function (path, index) {
        if(index == 0) return '';
        var location = {lat: path[0].lat, lng: path[0].lng, title: "center marker"}
        return <Marker key={index} map={that.state.map} maps={that.state.maps} marker={location} />;
      })
    }
    if (this.state.mapLoaded && this.state.trees && this.state.trees.length > 0){
      var that = this;
      var treeList = this.state.trees.map(function(tree, index){
        var location = {lat: tree[0], lng: tree[1], icon: that.props.tree}
        return <Marker key={'tree'+index} map={that.state.map} maps={that.state.maps} marker={location} />;
      })
    }
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '70vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: GoogleMapKey.key }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          onClick={this.onClick}
          onGoogleApiLoaded ={({ map, maps }) => { this.setState({ map: map, maps:maps, mapLoaded: true }) }}
          yesIWantToUseGoogleMapApiInternals
        >
        { this.state.mapLoaded && treeList }
        { this.state.mapLoaded && pathList }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.start} /> }
        { this.state.mapLoaded && intermediateMarkerList }
        { this.state.mapLoaded && <Marker map={this.state.map} maps={this.state.maps} marker={this.state.destination} /> }

        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;