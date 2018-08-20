import React, { Component } from 'react';
import { Button, ButtonGroup, Row, Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';

class MapOperations extends Component {

  constructor(props) {
    super(props);
    
    this.onRadioBtnClick = this.onRadioBtnClick.bind(this);
    this.toggleDropdown = this.toggleDropdown.bind(this);
    this.selectDropdownValue = this.selectDropdownValue.bind(this);
    this.onCheckboxBtnClick = this.onShowAttributeSelected.bind(this);

    this.state = { 
      rSelected: MapOperations.operations.none, 
      dropdownOpen: false,
      algorithmId: 0,
      attributeSelected: []
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
    1: "Least Hops",
    2: "Center Pass",
    3: "Scenic: Trees",
    4: "Scenic: Air Pollution",
    5: "Scenic: Cleanliness (Litter)",
    6: "Scenic: Trees + Air + Litter",
    7: "Scenic (Multi): Trees + Air + Litter",
    8: "Shortest Distance (Multi)",
    9: "Scenic (Multi): Trees",
    10: "Scenic (Multi): Air Pollution",
    11: "Scenic (Multi): Cleanliness (Litter)",
  };

  static attributeTexts = {
    0: "Trees", 
    1: "Cleanliness",
    2: "Air Pollution",
    3: "Random POIs"
  };

  static attributeIds = {
    trees: 0, 
    cleanliness: 1,
    airpollution: 2,
    candidates: 3
  };

  selectDropdownValue(algorithmId, operationValue) {
    this.setState({algorithmId: algorithmId});
    this.props.sendPathAlgorithm(algorithmId);
  }
  
  onShowAttributeSelected(selected) {
    const index = this.state.attributeSelected.indexOf(selected);
    if (index < 0) {
      console.log("Selected " + selected)
      this.state.attributeSelected.push(selected);
      this.props.sendAttributeSelection(selected, MapOperations.attributeTexts[selected], true);
    } else {
      console.log("Unselected " + selected)
      this.state.attributeSelected.splice(index, 1);
      this.props.sendAttributeSelection(selected, MapOperations.attributeTexts[selected], false);
    }
    this.setState({ attributeSelected: [...this.state.attributeSelected] });
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
              {/* <DropdownItem onClick={() => this.selectDropdownValue(2, "Center Pass")}
                  active={this.state.algorithmId === 2}>{MapOperations.algorithmTexts[2]}</DropdownItem> */}
              <DropdownItem onClick={() => this.selectDropdownValue(3, "Scenic: Trees")}
                  active={this.state.algorithmId === 3}>{MapOperations.algorithmTexts[3]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(4, "Scenic: Air Pollution")}
                  active={this.state.algorithmId === 4}>{MapOperations.algorithmTexts[4]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(5, "Scenic: Cleanliness (Litter)")}
                  active={this.state.algorithmId === 5}>{MapOperations.algorithmTexts[5]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(6, "Scenic: Trees + Air + Litter")}
                  active={this.state.algorithmId === 6}>{MapOperations.algorithmTexts[6]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(7, "Scenic (Multi): Trees + Air + Litter")}
                  active={this.state.algorithmId === 7}>{MapOperations.algorithmTexts[7]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(8, "Shortest Distance (Multi)")}
                  active={this.state.algorithmId === 8}>{MapOperations.algorithmTexts[8]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(9, "Scenic (Multi): Trees")}
                  active={this.state.algorithmId === 9}>{MapOperations.algorithmTexts[9]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(10, "Scenic (Multi): Air Pollution")}
                  active={this.state.algorithmId === 10}>{MapOperations.algorithmTexts[10]}</DropdownItem>
              <DropdownItem onClick={() => this.selectDropdownValue(11, "Scenic (Multi): Cleanliness (Litter)")}
                  active={this.state.algorithmId === 11}>{MapOperations.algorithmTexts[11]}</DropdownItem>
            </DropdownMenu>
          </Dropdown>
          &nbsp;
          <ButtonGroup>
            <Button color="success" onClick={() => this.onShowAttributeSelected(0)} active={this.state.attributeSelected.includes(0)}>{MapOperations.attributeTexts[0]}</Button>
            &nbsp;
            <Button color="success" onClick={() => this.onShowAttributeSelected(1)} active={this.state.attributeSelected.includes(1)}>{MapOperations.attributeTexts[1]}</Button>
            &nbsp;
            <Button color="success" onClick={() => this.onShowAttributeSelected(2)} active={this.state.attributeSelected.includes(2)}>{MapOperations.attributeTexts[2]}</Button>
            &nbsp;
            <Button color="warning" onClick={() => this.onShowAttributeSelected(3)} active={this.state.attributeSelected.includes(3)}>{MapOperations.attributeTexts[3]}</Button>
          </ButtonGroup>
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