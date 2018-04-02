import React, { Component } from 'react';
import { Button, Row } from 'reactstrap';

class MapOperations extends Component {

  constructor(props) {
    super(props);
    this.onRadioBtnClick = this.onRadioBtnClick.bind(this);
    this.state = { rSelected: MapOperations.operations.none };
  }

  static operations = {
    none: 0, 
    selectStart: 1,
    selectDestination: 2
  };

  onRadioBtnClick(rSelected) {
    this.setState({ rSelected });
    this.props.sendOperation(rSelected);
  }

  render() {
    return (
      <div style={{ height: '60vh', width: '100%' }}>

        <Row>
          <Button color="primary" size="sm" onClick={() => this.onRadioBtnClick(MapOperations.operations.selectStart)} 
                  active={this.state.rSelected === MapOperations.operations.selectStart}>Select Start</Button>
          &nbsp;
          <Button color="primary" size="sm" onClick={() => this.onRadioBtnClick(MapOperations.operations.selectDestination)} 
                  active={this.state.rSelected === MapOperations.operations.selectDestination}>Select Destination</Button>
        </Row>

        <Row>
          <div style={{ marginTop: '8px'}}>
            {this.state.rSelected === MapOperations.operations.selectStart && <p> Select starting point on map. </p>}
            {this.state.rSelected === MapOperations.operations.selectDestination && <p> Select destination point on map. </p>}
          </div>
        </Row>

      </div>
    );
  }
}

export default MapOperations;