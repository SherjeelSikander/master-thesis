import React, { Component } from 'react';
import './Map.css';
import SimpleMap from "./SimpleMap"
import MapOperations from "./MapOperations"
import { Container, Row, Col } from 'reactstrap'; 

class Map extends Component {

  constructor() {
    super();
    this.getOperation = this.getOperation.bind(this);
  }

  getOperation(val){
    console.log("Get Operation");
    console.log(val);
  }

  render() {
    return (
      <div className="Map">
        <header className="Map-header">
          <h1 className="Map-title">Tourist Route Recommender</h1>
        </header>
        <Container>
          <Row>              
            <Col xs="8"> <SimpleMap/>  </Col>
            <Col xs="4"> <MapOperations sendOperation={this.getOperation} /> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Map;
