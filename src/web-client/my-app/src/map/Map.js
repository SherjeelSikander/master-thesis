import React, { Component } from 'react';
import './Map.css';
import SimpleMap from "./SimpleMap"
import MapOperations from "./MapOperations"
import { Container, Row, Col } from 'reactstrap'; 
import axios from 'axios';
import { withAlert } from 'react-alert'

class Map extends Component {

  constructor() {
    super();
    this.getOperation = this.getOperation.bind(this);
    this.getResult = this.getResult.bind(this);
    this.getPathAlgorithm = this.getPathAlgorithm.bind(this);
    this.getAttributeSelection = this.getAttributeSelection.bind(this);
    this.state = {
      operation: MapOperations.operations.none,
      algorithmId: 0
    };
  }

  isStartDestinationValid(){
    var state = this.refs.simpleMap.state;
    if(state.start.lat !== 0 && state.start.lng !== 0 && state.destination.lat !== 0 && state.destination.lng !== 0){
      return true;
    } else{
      console.log("Start or Destination point is missing");
      return false;
    }
  }

  getOperation(operation){
    if(operation === MapOperations.operations.calculate){
      if(this.isStartDestinationValid()){
        var state = this.refs.simpleMap.state;
        var localhost = 'http://127.0.0.1:5000/';
        console.log("From: " + state.start.lat + ", " + state.start.lng + " to " +  state.destination.lat + ", " + state.destination.lng);
        console.log("AlgorithmID: " + this.state.algorithmId)
        axios.get(localhost + 'route/?startLat='+state.start.lat+'&startLng='+state.start.lng+'&destinationLat='+state.destination.lat+'&destinationLng='+state.destination.lng+'&algorithmId='+this.state.algorithmId)
        .then(response => {
          console.log("Response:")
          console.log(response.data)
          if(response.data.status == 422){
              this.props.alert.error(response.data.description);
              console.log(response.data.description)
          }else {
            var paths = []
            for (var i = 0; i < response.data.length; i++) {
              var data = response.data[i]
              var path = []
              for (var j = 0; j < data.length; j++) {
                path.push({lat: parseFloat(data[j][0]), lng: parseFloat(data[j][1])})
              }
              paths.push(path)
            }
            this.setState({ paths: paths });
          }          
        })
      }
    } else {
      this.setState({ operation: operation });
    }
  }

  getResult(result){
    this.setState({ result: result });
    this.refs.mapOperations.clearSelection();
  }

  getPathAlgorithm(algorithmId){
    this.setState({ algorithmId: algorithmId });
  }

  getAttributeSelection(attributeId, attributeText, show){
    console.log(attributeId + " " + attributeText + " " + show);
    var localhost = 'http://127.0.0.1:5000/';
    if(attributeId === MapOperations.attributeIds.trees){
      if(show == true){
        console.log("Show trees")
        axios.get(localhost + 'trees/')
        .then(response => {
          console.log("Response:")
          console.log(response.data)
          this.setState({ trees: response.data });      
        })          
      } else if (show == false){
          console.log("Hide trees")
      }
    }
  }

  render() {
    return (
      <div className="Map">
        <header className="Map-header">
          <h1 className="Map-title">Tourist Route Recommender</h1>
        </header>
        <Container>
          <Row>              
            <Col xs="12"> <SimpleMap ref="simpleMap" paths={this.state.paths} trees={this.state.trees} operation={this.state.operation} sendResult={this.getResult}/>  </Col>
            <Col xs="12"> &nbsp; </Col>
            <Col xs="12"> <MapOperations ref="mapOperations" result={this.state.result} sendOperation={this.getOperation} sendPathAlgorithm={this.getPathAlgorithm} sendAttributeSelection={this.getAttributeSelection}/> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default withAlert(Map);
