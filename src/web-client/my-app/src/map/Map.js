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
        this.setState({ candidates: state.candidates });
        axios.get(localhost + 'route/?startLat='+state.start.lat+'&startLng='+state.start.lng+'&destinationLat='+state.destination.lat+'&destinationLng='+state.destination.lng+'&algorithmId='+this.state.algorithmId+'&candidates='+state.candidates)
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
    } else if(operation === MapOperations.operations.clearPOIs){
      this.setState({ candidates: [] });
    }else{
      this.setState({ operation: operation });
    }
  }

  getResult(result){
    this.setState({ result: result });
    this.setState({ operation: MapOperations.operations.none });
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
          this.setState({ trees: [] });  
      }
    } else if (attributeId === MapOperations.attributeIds.airpollution){
      if(show == true){
        console.log("Show Air Pollution")
        axios.get(localhost + 'airpollution/')
        .then(response=> {
          console.log("Response")
          console.log(response.data)
          this.setState({ airpollution: response.data });
        })
      } else if (show == false){
          console.log("Hide air pollution")
          this.setState({ airpollution: [] });
      } 
    } else if (attributeId === MapOperations.attributeIds.cleanliness){
      if(show == true){
        console.log("Show Cleanliness")
        axios.get(localhost + 'litter/')
        .then(response=> {
          console.log("Response")
          console.log(response.data)
          this.setState({ cleanliness: response.data });
        })
      } else if (show == false){
        console.log("Hide cleanliness")
        this.setState({ cleanliness: [] });
      } 
    } else if (attributeId === MapOperations.attributeIds.candidates){
      console.log("Show Random Candidates")
      axios.get(localhost + 'candidates/')
      .then(response=> {
        console.log("Response")
        console.log(response.data)
        this.setState({ candidates: response.data });
      })
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
            <Col xs="12"> <SimpleMap ref="simpleMap" paths={this.state.paths} trees={this.state.trees} airpollution={this.state.airpollution} cleanliness={this.state.cleanliness} candidates={this.state.candidates} operation={this.state.operation} sendResult={this.getResult}/>  </Col>
            <Col xs="12"> &nbsp; </Col>
            <Col xs="12"> <MapOperations ref="mapOperations" result={this.state.result} sendOperation={this.getOperation} sendPathAlgorithm={this.getPathAlgorithm} sendAttributeSelection={this.getAttributeSelection}/> </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default withAlert(Map);
