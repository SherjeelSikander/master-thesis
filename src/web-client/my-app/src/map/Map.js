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
    this.state = {
      operation: MapOperations.operations.none
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
        axios.get(localhost + 'route/?startLat='+state.start.lat+'&startLng='+state.start.lng+'&destinationLat='+state.destination.lat+'&destinationLng='+state.destination.lng)
        .then(response => console.log(response))
      }
    } else {
      this.setState({ operation: operation });
    }
  }

  getResult(result){
    this.setState({ result: result });
    this.refs.mapOperations.clearSelection();
  }

  render() {
    return (
      <div className="Map">
        <header className="Map-header">
          <h1 className="Map-title">Tourist Route Recommender</h1>
        </header>
        <Container>
          <Row>              
            <Col xs="8"> <SimpleMap ref="simpleMap" operation={this.state.operation} sendResult={this.getResult}/>  </Col>
            <Col xs="4"> <MapOperations ref="mapOperations" result={this.state.result} sendOperation={this.getOperation} /> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Map;
