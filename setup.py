from setuptools import find_packages, setup

package_name = 'recorded_odometry_publisher_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='esl',
    maintainer_email='23557702@sun.ac.za',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "recorded_odom_pub = recorded_odometry_publisher_py.recorded_odom_pub:main"
        ],
    },
)
