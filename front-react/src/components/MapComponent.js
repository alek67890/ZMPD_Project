import React from 'react';
import { connect } from 'react-redux';


class MapComponent extends React.Component {


    componentDidMount(){
    
    }

    render (){
        if (this.props.data.iss_position){
            this.updateMap(this.props.data)
        }
        
        return (
            <div>
                <h1>Map</h1>
                <div id="map"></div>
            </div>
        )
    }

}


const mapStateToProps = state => {
    return { 
        data: state.data,
    };
  };
  
export default connect(
  mapStateToProps,
  {  }
)(MapComponent);
