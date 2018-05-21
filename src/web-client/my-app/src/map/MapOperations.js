import React, { Component } from 'react';
import { Button, Row, Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';

class MapOperations extends Component {

  constructor(props) {
    super(props);
    
    this.onRadioBtnClick = this.onRadioBtnClick.bind(this);
    this.toggleDropdown = this.toggleDropdown.bind(this);
    this.selectDropdownValue = this.selectDropdownValue.bind(this);
    
    this.state = { 
      rSelected: MapOperations.operations.none, 
      dropdownOpen: false,
      algorithmId: 0
    };
  }

  static operations = {
    none: 0, 
    selectStart: 1,
    selectDestination: 2,
    clear: 3, 
    calculate: 4,
    selectCalculationType: 5
  };

  clearSelection(){
    this.setState({ rSelected: MapOperations.operations.clear });
  }

  onRadioBtnClick(rSelected) {
    this.setState({ rSelected });
    this.props.sendOperation(rSelected);
  }

  calculate(){
    this.props.sendOperation(MapOperations.operations.calculate);
  }

  toggleDropdown() {
    this.setState(prevState => ({
      dropdownOpen: !prevState.dropdownOpen
    }));
  }

  static algorithmTexts = {
    0: "Shortest Distance", 
    1: "Least Hops"
  };

  selectDropdownValue(algorithmId, operationValue) {
    this.setState({algorithmId: algorithmId});
    this.props.sendPathAlgorithm(algorithmId);
  }
  

  render() {
    return (
      <div style={{ height: '100%', width: '100%' }}>

        <Row>
          <Button color="primary" size="sm" onClick={() => this.onRadioBtnClick(MapOperations.operations.selectStart)} 
                  active={this.state.rSelected === MapOperations.operations.selectStart}>Select Start</Button>
          &nbsp;
          <Button color="primary" size="sm" onClick={() => this.onRadioBtnClick(MapOperations.operations.selectDestination)} 
                  active={this.state.rSelected === MapOperations.operations.selectDestination}>Select Destination</Button>
          &nbsp;
          <Button color="primary" size="sm" onClick={() => this.calculate()}>Calculate</Button>
          &nbsp;
          <Dropdown isOpen={this.state.dropdownOpen} toggle={this.toggleDropdown}>
            <DropdownToggle caret>
              {MapOperations.algorithmTexts[this.state.algorithmId]}
            </DropdownToggle>
            <DropdownMenu>
              <DropdownItem onClick={() => this.selectDropdownValue(0, "Shortest Distance")}
                  active={this.state.algorithmId === 0}>{MapOperations.algorithmTexts[0]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(1, "Least Hops")}
                  active={this.state.algorithmId === 1}>{MapOperations.algorithmTexts[1]}</DropdownItem>
            </DropdownMenu>
          </Dropdown>
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