�
    *!g�  �                   �   � d dl Zd� Zd� Zd� Zy)�    Nc                  �  � t        j                  ddd��      } g }t        j                  d| � d��       t        | �      D ]4  }t        j                  d|dz   � d�d|� ���      }|j	                  |�       �6 g }t        j                  d	| � d��       t        | �      D ]4  }t        j                  d
|dz   � d�d|� ���      }|j	                  |�       �6 ||fS )NuA   Ingrese el tamaño de los vectores (deben ser del mismo tamaño):�   )�	min_value�stepu1   Ingrese los elementos del vector fila de tamaño �:zElemento fila �fila_)�keyu4   Ingrese los elementos del vector columna de tamaño zElemento columna �columna_)�st�number_input�write�range�append)�n�fila�i�elemento�columnas        �BC:\Users\jesyg\Downloads\app.py\modulos\multiplicacion_vectores.py�ingresar_vectoresr      s�   � �
���[�gh�op�q�A� �D��H�H�@���1�E�F��1�X���?�?�^�A�a�C�5��#:�%��s��L�����H�� �
 �G��H�H�C�A�3�a�H�I��1�X���?�?�%6�q��s�e�1�#=�X�a�S�>�R�����x� � � ��=��    c                 �  � t        d� t        | |�      D �       �      }t        t        | �      �      D �cg c]  }| |   � d||   � ��� }}t	        j
                  d�       t	        j
                  ddj                  |�      � d|� ��       |S c c}w )Nc              3   �,   K  � | ]  \  }}||z  �� � y �w)N� )�.0�f�cs      r   �	<genexpr>z'multiplicar_vectores.<locals>.<genexpr>   s   � �� �>�+=�4�1�a��Q��+=�s   ��*u0   
Realizando la multiplicación fila por columna:zResultado: z + z = )�sum�zipr   �lenr   r   �join)r   r   �producto_puntor   �termino_matematicos        r   �multiplicar_vectoresr&      s�   � ��>�3�t�W�+=�>�>�N�=B�3�t�9�=M�N�=M��T�!�W�I�Q�w�q�z�l�3�=M��N� �H�H�@�A��H�H�{�5�:�:�&8�9�:�#�n�=M�N�O���� Os   �B
c                  �  � t        j                  d�       t        �       \  } }| rP|rNt        | �      t        |�      k(  r7t	        | |�      }t        j
                  d�       t        j
                  |�       y t        j
                  d�       y )Nu.   Multiplicación de vectores (Fila por Columna)uG   
Resultado de la multiplicación del vector fila por el vector columna:u"   Ingrese vectores de igual tamaño.)r   �headerr   r"   r&   r   )r   r   r$   s      r   �multiplicacion_de_vectoresr)   "   sa   � ��I�I�>�?�%�'�M�D�'���C��I��W��5�-�d�G�<��
���[�\�
���� �
���5�6r   )�	streamlitr   r   r&   r)   r   r   r   �<module>r+      s   �� ��(	�	7r   