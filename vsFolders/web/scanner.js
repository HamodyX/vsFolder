const axios = require('axios');

const SKYSCANNER_API_URL = 'https://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/SE/SEK/en-US/STO/anywhere/anytime/anytime';
const API_KEY = 'YOUR_SKYSCANNER_API_KEY'; // Replace with your Skyscanner API key

const getFlightData = async () => {
  try {
    const response = await axios.get(SKYSCANNER_API_URL, {
      headers: {
        'X-Api-Key': API_KEY,
      },
    });

    const flights = response.data.Quotes.filter(
      (quote) =>
        quote.OutboundLeg &&
        quote.OutboundLeg.DestinationId === 'JED-sky' &&
        quote.OutboundLeg.OriginId === 'ARN-sky'
    );

    flights.forEach((flight) => {
      console.log(
        `From: ${flight.OutboundLeg.OriginId} To: ${flight.OutboundLeg.DestinationId} Price: ${flight.MinPrice}`
      );
    });
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

getFlightData();
