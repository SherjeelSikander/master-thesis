import { PureComponent } from 'react';

class Marker extends PureComponent {

    componentWillUpdate() {
      this.marker = null;
    }
  
    componentWillUnmount() {
      this.marker = null;
    }
  
    getPosition() {
      return { lat: 48.1496636, lng: 11.5656715 };      
    }
  
    render = () => {
      const Marker = this.props.maps.Marker;
  
      const position = { position: this.getPosition() };
      const map = { map: this.props.map }
      const title = { title: "Hello Marker" }

      this.marker = new Marker(Object.assign({}, position, map, title));
  
      return null
    }
  }

  export default Marker;