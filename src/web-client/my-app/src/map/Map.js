import React, { Component } from 'react';
import './Map.css';
import SimpleMap from "./SimpleMap"
import MapOptions from "./MapOptions"
import { Container, Row, Col } from 'reactstrap'; 

class Map extends Component {
  render() {
    return (
      <div className="Map">
        <header className="Map-header">
          <h1 className="Map-title">Tourist Route Recommender</h1>
        </header>
        <Container>
          <Row>              
            <Col xs="8"> <SimpleMap/>  </Col>
            <Col xs="4"> <MapOptions/> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Map;
