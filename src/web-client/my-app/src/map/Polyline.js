import { PureComponent } from 'react';

class Polyline extends PureComponent {

  componentWillUpdate() {
    this.line.setMap(null)
  }

  componentWillUnmount() {
    this.line.setMap(null)
  }

  getPath() {
    if (this.props.path && this.props.path.length > 2) {
      return this.props.path;
    } else {
      return [];
    }
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