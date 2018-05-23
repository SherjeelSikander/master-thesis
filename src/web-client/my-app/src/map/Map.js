import React, { Component } from 'react';
import './Map.css';
import SimpleMap from "./SimpleMap"
import MapOperations from "./MapOperations"
import { Container, Row, Col } from 'reactstrap'; 
import axios from 'axios';

class Map extends Component {

  constructor() {
    super();
    this.getOperation = this.getOperation.bind(this);
    this.getResult = this.getResult.bind(this);
    this.getPathAlgorithm = this.getPathAlgorithm.bind(this);
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
          if(response.status){
              console.log(response.data.description)
          }else {
            var path = [];
            for (var i = 0; i < response.data.length; i++) {
              path.push({lat: parseFloat(response.data[i][0]), lng: parseFloat(response.data[i][1])})
            }
            this.setState({ path: path });
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

  render() {
    return (
      <div className="Map">
        <header className="Map-header">
          <h1 className="Map-title">Tourist Route Recommender</h1>
        </header>
        <Container>
          <Row>              
            <Col xs="12"> <SimpleMap ref="simpleMap" path={this.state.path} operation={this.state.operation} sendResult={this.getResult}/>  </Col>
            <Col xs="12"> &nbsp; </Col>
            <Col xs="12"> <MapOperations ref="mapOperations" result={this.state.result} sendOperation={this.getOperation} sendPathAlgorithm={this.getPathAlgorithm}/> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Map;
