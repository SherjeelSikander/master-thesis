import React, { Component } from 'react';
import './Map.css';
import SimpleMap from "./SimpleMap"
import MapOperations from "./MapOperations"
import { Container, Row, Col } from 'reactstrap'; 

class Map extends Component {

  constructor() {
    super();
    this.getOperation = this.getOperation.bind(this);
    this.getResult = this.getResult.bind(this);
    this.state = {
      operation: MapOperations.operations.none
    };
  }

  getOperation(operation){
    this.setState({ operation: operation });
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
            <Col xs="8"> <SimpleMap operation={this.state.operation} sendResult={this.getResult}/>  </Col>
            <Col xs="4"> <MapOperations ref="mapOperations" result={this.state.result} sendOperation={this.getOperation} /> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Map;
