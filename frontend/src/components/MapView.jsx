import DeckGL from "@deck.gl/react";
import { GeoJsonLayer } from "@deck.gl/layers";
import Map from "react-map-gl/maplibre";
import "maplibre-gl/dist/maplibre-gl.css";

// Sample disease data
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
    },
    {
      type: "Feature",
      properties: {
        disease: "Leaf Spot"
      },
      geometry: {
        type: "Polygon",
        coordinates: [[
          [83.32, 17.71],
          [83.34, 17.71],
          [83.34, 17.73],
          [83.32, 17.73],
          [83.32, 17.71]
        ]]
      }
    }
  ]
};

// Disease map layers
function MapView() {
  const layers = [
    new GeoJsonLayer({
      id: "fungal-blight",
      data: {
        ...sampleData,
        features: sampleData.features.filter(
          (f) => f.properties.disease === "Fungal Blight"
        )
      },
      filled: true,
      stroked: true,
      getFillColor: [255, 0, 0, 120],
      getLineColor: [200, 0, 0],
      lineWidthMinPixels: 2
    }),

    new GeoJsonLayer({
      id: "leaf-spot",
      data: {
        ...sampleData,
        features: sampleData.features.filter(
          (f) => f.properties.disease === "Leaf Spot"
        )
      },
      filled: true,
      stroked: true,
      getFillColor: [255, 200, 0, 120],
      getLineColor: [200, 150, 0],
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
          pitch: 0,
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