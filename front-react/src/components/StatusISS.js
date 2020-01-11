import React from 'react';
import { connect } from 'react-redux';
import { fetchFirstData, fetchDataAndCal } from '../store/actions';


class StatusISS extends React.Component {

    componentDidMount() {
        this.props.fetchFirstData();
        this.interval = setInterval(() => this.tick(), 3000);
    }

    tick() {
        this.props.fetchDataAndCal();
    }


    componentWillUnmount() {
        clearInterval(this.interval);
    }


    render (){
        let distance = this.props.distance.toFixed(2);
        let speed = this.props.speed.toFixed(2);
        return (
            <div>
                <h1>Status of ISS</h1>
                <img className="photo" src='/iss.jpg' alt='ISS'></img>
                <h2>ISS travel {distance} km in last {this.props.time}<br/>
                Average speed* = {speed} km/h</h2>
            </div>
        )
    }

}

const mapStateToProps = state => {
    return { 
        data: state.data,
        time: state.time,
        distance: state.distance,
        speed: state.speed,
    };
  };
  
export default connect(
  mapStateToProps,
  { fetchFirstData, fetchDataAndCal }
)(StatusISS);

