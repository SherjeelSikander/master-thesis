import React, { Component } from 'react';
import './Map.css';
import SimpleMap from "./SimpleMap"

class Map extends Component {
  render() {
    return (
      <div className="Map">
        <header className="Map-header">
          <h1 className="Map-title">Tourist Route Recommender</h1>
        </header>
        <SimpleMap />
      </div>
    );
  }
}

export default Map;
