# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
	main_dir = get_package_share_directory('ackermann_simulation')

	urdf_path = os.path.join(main_dir, 'models', 'ackermann_model', 'ackermann_model.urdf')
	xacro_path = os.path.join(main_dir, 'urdf', 'ackermann_model.urdf.xacro')

	return LaunchDescription([
		ExecuteProcess(
			cmd=[['ros2 run xacro xacro ',
						str(xacro_path),
						' > ',
						str(urdf_path),
						]],
      output="screen",
      emulate_tty=True,
			shell=True,
		),
	])
