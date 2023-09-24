import java.io.*;
import java.net.*;

public class UDPVideoReceiver {
    public static void main(String[] args) {
        int port = 4212;
        String outputFileName = "received_video.avi"; // Nombre del archivo de salida

        try {
            DatagramSocket socket = new DatagramSocket(port);
            FileOutputStream fileOutputStream = new FileOutputStream(outputFileName);

            byte[] buffer = new byte[1024]; // Tamaño del búfer para recibir datos

            System.out.println("Esperando la recepción del video en el puerto " + port);

            // Indicar que la conexión se ha establecido
            System.out.println("Conexión establecida. Esperando paquetes...");

            int packetCount = 0;

            while (true) {
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet); // Recibir un paquete UDP

                // Escribir los datos recibidos en el archivo de salida
                fileOutputStream.write(packet.getData(), 0, packet.getLength());

                // Mostrar mensaje de paquete recibido
                System.out.println("Paquete " + (packetCount + 1) + " recibido.");
                packetCount++;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
