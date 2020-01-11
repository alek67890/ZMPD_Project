import React from 'react'
// import ReactDOM from 'react-dom'
import Plotly from 'plotly.js-basic-dist'


import createPlotlyComponent from 'react-plotly.js/factory';
const Plot = createPlotlyComponent(Plotly); 

class PlotCompoment extends React.Component {
  constructor(props){
    super(props);

    this.state = {
      data : [],
      };
}

componentDidMount(){

  let routes = this.props.routes_plot

  routes = routes.map((route) => {
    return {
      x: route[0],
      y: route[1],
      mode: 'lines',
      type: 'scatter'
    }
  })

  let tracks = {
    name: 'points',
    x: this.props.points[0],
    y: this.props.points[1],
    mode: 'markers',
    type: 'scatter'
  };

  let data = [tracks, ...routes]
  this.setState({data : data}) 

}
  render () {
    // console.log(this.props.points)
    // console.log(this.props.routes_plot)
    
    // console.log(this.state.data)
    return <div>
      <Plot
        data={this.state.data}
        layout={ {width: 600, height: 400, title: this.props.name+ ' Routes'} }
      />
    </div>
  }
}

export default PlotCompoment;