import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import './Timeline.css';

const Timeline = ({ data, currentTime, onTimeChange }) => {
  const svgRef = useRef();
  const [dimensions, setDimensions] = useState({ width: 800, height: 400 });

  useEffect(() => {
    if (!data || !data.timeline) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll('*').remove();

    const { width, height } = dimensions;
    const margin = { top: 20, right: 30, bottom: 30, left: 40 };

    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    // Create scales
    const xScale = d3.scaleTime()
      .domain(d3.extent(data.timeline, d => new Date(d.timestamp * 1000)))
      .range([0, innerWidth]);

    const yScale = d3.scaleLinear()
      .domain([0, d3.max(data.timeline, d => d.cumulative_lines)])
      .range([innerHeight, 0]);

    // Create main group
    const g = svg.append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Add X axis
    g.append('g')
      .attr('transform', `translate(0,${innerHeight})`)
      .call(d3.axisBottom(xScale));

    // Add Y axis
    g.append('g')
      .call(d3.axisLeft(yScale));

    // Add line for cumulative lines
    const line = d3.line()
      .x(d => xScale(new Date(d.timestamp * 1000)))
      .y(d => yScale(d.cumulative_lines));

    g.append('path')
      .datum(data.timeline)
      .attr('fill', 'none')
      .attr('stroke', '#007bff')
      .attr('stroke-width', 2)
      .attr('d', line);

    // Add commit points
    g.selectAll('.commit-point')
      .data(data.timeline)
      .enter()
      .append('circle')
      .attr('class', 'commit-point')
      .attr('cx', d => xScale(new Date(d.timestamp * 1000)))
      .attr('cy', d => yScale(d.cumulative_lines))
      .attr('r', 4)
      .attr('fill', '#007bff')
      .attr('stroke', '#fff')
      .attr('stroke-width', 2);

  }, [data, dimensions]);

  useEffect(() => {
    const handleResize = () => {
      const container = svgRef.current?.parentElement;
      if (container) {
        setDimensions({
          width: container.clientWidth,
          height: container.clientHeight
        });
      }
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <div className="timeline-wrapper">
      <svg
        ref={svgRef}
        width={dimensions.width}
        height={dimensions.height}
        className="timeline-svg"
      />
    </div>
  );
};

export default Timeline;