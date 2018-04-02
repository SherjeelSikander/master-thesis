import { PureComponent } from 'react';

class Marker extends PureComponent {

    componentWillUpdate() {
        this.marker.setMap(null)
    }
  
    componentWillUnmount() {
        this.marker.setMap(null);
    }
  
    getTestPosition() { //test marker
        return { lat: 48.1496636, lng: 11.5656715 };      
    }
  
    render() {
        const Marker = this.props.maps.Marker;

        const position = { position: this.props.marker }; // { position: this.getTestPosition() };
        const map = { map: this.props.map };
        const title = { title: this.props.marker.title };
        if(this.props.marker.icon) {
            const icon = { icon: this.props.marker.icon } 
            this.marker = new Marker(Object.assign({}, position, map, title, icon));
        } else {
            this.marker = new Marker(Object.assign({}, position, map, title));
        }

        return null
    }
  }

  export default Marker;