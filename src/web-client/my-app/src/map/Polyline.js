import { PureComponent } from 'react';

class Polyline extends PureComponent {

    componentWillUpdate() {
      this.line.setMap(null)
    }
  
    componentWillUnmount() {
      this.line.setMap(null)
    }
  
    getPath() {
      return [
        { lat: 48.1496636, lng: 11.5656715 },
        { lat: 48.1596636, lng: 11.5756715 }, 
        { lat: 48.1496636, lng: 11.5856715 }
      ];
    }

    getAttributes() {
        return {
            geodesic: true,
            strokeColor: this.props.color || '#000000',
            strokeOpacity: 1,
            strokeWeight: 4
          }
    }
  
    render = () => {
      const Polyline = this.props.maps.Polyline;
  
      const attributes = this.getAttributes();
      const paths = { path: this.getPath() };
      this.line = new Polyline(Object.assign({}, attributes, paths));

      this.line.setMap(this.props.map);
  
      return null
    }
  }

  export default Polyline;