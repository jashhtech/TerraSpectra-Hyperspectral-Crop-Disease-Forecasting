import DeckGL from "@deck.gl/react";
import { GeoJsonLayer } from "@deck.gl/layers";
import Map from "react-map-gl/maplibre";
import "maplibre-gl/dist/maplibre-gl.css";

const sampleData = {
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: {
        disease: "Fungal Blight"
      },
      geometry: {
        type: "Polygon",
        coordinates: [[
          [83.29, 17.71],
          [83.31, 17.71],
          [83.31, 17.73],
          [83.29, 17.73],
          [83.29, 17.71]
        ]]
      }
    }
  ]
};

function MapView() {
  const layers = [
    new GeoJsonLayer({
      id: "disease-overlay",
      data: sampleData,
      filled: true,
      stroked: true,
      getFillColor: [255, 0, 0, 110],
      getLineColor: [200, 0, 0],
      lineWidthMinPixels: 2
    })
  ];

  return (
    <div style={{ height: "450px", width: "100%" }}>
      <DeckGL
        initialViewState={{
          longitude: 83.30,
          latitude: 17.72,
          zoom: 13,
          pitch: 30,
          bearing: 0
        }}
        controller={true}
        layers={layers}
      >
        <Map
          mapStyle="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
        />
      </DeckGL>
    </div>
  );
}

export default MapView;