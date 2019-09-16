import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  int count = 0;
  incrClick = () => {
    count++;
    alert('count has been incremented')
  }
  decrClick = () => {
    count--;
    alert('count has been decremented')
  }
  render() {
    return (
      <div>
        <label>{count}</label>
        <button onClick={this.incrClick}>increment</button>
        <button onClick={this.decrClick}>decrement</button>
      <div/>
    )
  }
}

export default Counter
