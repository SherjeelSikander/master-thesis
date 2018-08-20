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
    else if(nextProps.trees && nextProps.trees.length === 0){
      this.setState({trees:[]})
    }
    if(nextProps.airpollution && nextProps.airpollution.length > 0){
      this.setState({airpollution:nextProps.airpollution})
    }
    else if(nextProps.airpollution && nextProps.airpollution.length === 0){
      this.setState({airpollution:[]})
    }
    if(nextProps.cleanliness && nextProps.cleanliness.length > 0){
      this.setState({cleanliness:nextProps.cleanliness})
    }
    else if(nextProps.cleanliness && nextProps.cleanliness.length === 0){
      this.setState({cleanliness:[]})
    } 
    if(nextProps.candidates && nextProps.candidates.length > 0){
      this.setState({candidates:nextProps.candidates})
    }
    else if(nextProps.candidates && nextProps.candidates.length === 0){
      this.setState({candidates:[]})
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
    tree: "https://maps.google.com/mapfiles/ms/micons/tree.png",
    litter: {
      green: "https://i.imgur.com/Dkp0VKi.png",
      orange: "https://i.imgur.com/njKaQIy.png",
      red: "https://i.imgur.com/PHDuhu0.png"
    },
    poi: "https://maps.google.com/mapfiles/kml/pal3/icon23.png"
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
    if (this.state.mapLoaded && this.state.candidates && this.state.candidates.length > 0){
      var that = this;
      var candidateList = this.state.candidates.map(function(candidate, index){
          var location = {lat: parseFloat(candidate[1][1],10), lng: parseFloat(candidate[1][2],10), icon: that.props.poi, title: candidate[1][0]}
          return <Marker key={'candidate'+index} map={that.state.map} maps={that.state.maps} marker={location} />;
      })
    }
    if (this.state.mapLoaded && this.state.cleanliness && this.state.cleanliness.length > 0){
      var that = this;
      var cleanlinessList = this.state.cleanliness.map(function(litter, index){
        var litterValue = parseInt(litter[2], 10)
        var iconUrl
        if (litterValue < 2) {
          iconUrl = that.props.litter.green
        } else if (litterValue < 5){
          iconUrl = that.props.litter.orange
        } else if (litterValue >= 5){
          iconUrl = that.props.litter.red
        }
        var location = {lat: litter[0], lng: litter[1], icon: iconUrl}
        return <Marker key={'litter'+index} map={that.state.map} maps={that.state.maps} marker={location} />;
      })
    }
    if (this.state.mapLoaded && this.state.airpollution && this.state.airpollution.length > 0){
      var that = this;
      var pollutionLines = this.state.airpollution.map(function(airpollution, index){
        var startLocation = {lat: airpollution[0], lng: airpollution[1]}
        var endLocation = {lat: airpollution[2], lng: airpollution[3]}
        var path = [startLocation, endLocation]
        var caqi = parseInt(airpollution[4], 10)
        var verylow = "#79bc6a"
        var low = "#bbcf4c"
        var medium = "#eec20b"
        var high = "#f29305"
        var veryhigh = "#e8416f"
        var color = verylow
        if(caqi < 25){
          color = verylow
        } else if (caqi < 50) {
          color = low
        } else if (caqi < 75) {
          color = medium
        } else if (caqi < 100){
          color = high
        } else if (caqi > 100) {
          color = veryhigh
        }
        
        return <Polyline key={'airpollution'+index} map={that.state.map} maps={that.state.maps} path={path} color={color}/>;
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
        { this.state.mapLoaded && pollutionLines }
        { this.state.mapLoaded && cleanlinessList }
        { this.state.mapLoaded && candidateList }
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